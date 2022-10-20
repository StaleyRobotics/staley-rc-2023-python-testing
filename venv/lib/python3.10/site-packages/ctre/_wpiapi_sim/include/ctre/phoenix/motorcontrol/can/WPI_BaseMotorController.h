/**
 * WPI Compliant motor controller class.
 * WPILIB's object model requires many interfaces to be implemented to use
 * the various features.
 * This includes...
 * - Software PID loops running in the robot controller
 * - LiveWindow/Test mode features
 * - Motor Safety (auto-turn off of motor if Set stops getting called)
 * - Single Parameter set that assumes a simple motor controller.
 */
#pragma once

#include "ctre/phoenix/motorcontrol/can/BaseMotorController.h"

//Need to disable certain warnings for WPI headers.
#if __GNUC__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#elif _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4522 4458 4522)
#endif

#include "wpi/sendable/Sendable.h"
#include "wpi/sendable/SendableHelper.h"
#include "frc/motorcontrol/MotorController.h"
#include "frc/MotorSafety.h"
#include "wpi/raw_ostream.h"
#include <mutex>
#include <hal/SimDevice.h>

//Put the warning settings back to normal
#if __GNUC__
#pragma GCC diagnostic pop
#elif _MSC_VER
#pragma warning(pop)
#endif

namespace ctre
{
namespace phoenix
{
namespace motorcontrol
{
namespace can
{

/**
 * VEX Victor SPX Motor Controller when used on CAN Bus.
 */
class WPI_BaseMotorController : public virtual BaseMotorController,
								public virtual frc::MotorController,
								public frc::MotorSafety,
								public wpi::Sendable,
								public wpi::SendableHelper<WPI_BaseMotorController>
{
  public:
	/**
	 * Constructor for a WPI_BaseMotorController
	 * @param deviceNumber Device ID of BaseMotorController
	 */
	WPI_BaseMotorController(int deviceNumber, const char *model);
	virtual ~WPI_BaseMotorController();

	WPI_BaseMotorController() = delete;
	WPI_BaseMotorController(WPI_BaseMotorController const &) = delete;
	WPI_BaseMotorController &operator=(WPI_BaseMotorController const &) = delete;

	//----------------------- set/get routines for WPILIB interfaces -------------------//
	/**
	 * Common interface for setting the speed of a simple speed controller.
	 *
	 * @param speed The speed to set.  Value should be between -1.0 and 1.0.
	 * 									Value is also saved for Get().
	 */
	virtual void Set(double speed);

	/**
	 * Common interface for getting the current set speed of a speed controller.
	 *
	 * @return The current set speed.  Value is between -1.0 and 1.0.
	 */
	virtual double Get() const;

	//----------------------- Intercept CTRE calls for motor safety -------------------//
	/**
	 * Sets the appropriate output on the talon, depending on the mode.
	 * @param mode The output mode to apply.
	 * In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
	 * In Current mode, output value is in amperes.
	 * In Velocity mode, output value is in position change / 100ms.
	 * In Position mode, output value is in encoder ticks or an analog value,
	 *   depending on the sensor.
	 * In Follower mode, the output value is the integer device ID of the talon to
	 * duplicate.
	 *
	 * @param value The setpoint value, as described above.
	 *
	 *
	 *	Standard Driving Example:
	 *	_talonLeft.set(ControlMode.PercentOutput, leftJoy);
	 *	_talonRght.set(ControlMode.PercentOutput, rghtJoy);
	 */
	virtual void Set(ControlMode mode, double value);
	/**
	 * @param mode Sets the appropriate output on the talon, depending on the mode.
	 * @param demand0 The output value to apply.
	 * 	such as advanced feed forward and/or auxiliary close-looping in firmware.
	 * In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
	 * In Current mode, output value is in amperes.
	 * In Velocity mode, output value is in position change / 100ms.
	 * In Position mode, output value is in encoder ticks or an analog value,
	 *   depending on the sensor. See
	 * In Follower mode, the output value is the integer device ID of the talon to
	 * duplicate.
	 *
	 * @param demand1Type The demand type for demand1.
	 * Neutral: Ignore demand1 and apply no change to the demand0 output.
	 * AuxPID: Use demand1 to set the target for the auxiliary PID 1.
	 * ArbitraryFeedForward: Use demand1 as an arbitrary additive value to the
	 *	 demand0 output.  In PercentOutput the demand0 output is the motor output,
	 *   and in closed-loop modes the demand0 output is the output of PID0.
	 * @param demand1 Supplmental output value.  Units match the set mode.
	 *
	 *
	 *  Arcade Drive Example:
	 *		_talonLeft.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, +joyTurn);
	 *		_talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, -joyTurn);
	 *
	 *	Drive Straight Example:
	 *	Note: Selected Sensor Configuration is necessary for both PID0 and PID1.
	 *		_talonLeft.follow(_talonRght, FollwerType.AuxOutput1);
	 *		_talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.AuxPID, desiredRobotHeading);
	 *
	 *	Drive Straight to a Distance Example:
	 *	Note: Other configurations (sensor selection, PID gains, etc.) need to be set.
	 *		_talonLeft.follow(_talonRght, FollwerType.AuxOutput1);
	 *		_talonRght.set(ControlMode.MotionMagic, targetDistance, DemandType.AuxPID, desiredRobotHeading);
	 */
	virtual void Set(ControlMode mode, double demand0, DemandType demand1Type, double demand1);


	/**
	 * Sets the voltage output of the SpeedController.  Compensates for
	 * the current bus voltage to ensure that the desired voltage is output even
	 * if the battery voltage is below 12V - highly useful when the voltage
	 * outputs are "meaningful" (e.g. they come from a feedforward calculation).
	 *
	 * <p>NOTE: This function *must* be called regularly in order for voltage
	 * compensation to work properly - unlike the ordinary set function, it is not
	 * "set it and forget it."
	 *
	 * @param output The voltage to output.
	 */
	virtual void SetVoltage(units::volt_t output);

	//----------------------- Invert routines -------------------//
	/**
	 * Common interface for inverting direction of a speed controller.
	 *
	 * @param isInverted The state of inversion, true is inverted.
	 */
	virtual void SetInverted(bool isInverted);
	/**
	 * Common interface for inverting direction of a speed controller.
	 *
	 * @param invertType The invert strategy to use. Follower controllers
	 * 					that mirror/oppose the master controller should 
	 *					use this method.
	 */
	virtual void SetInverted(InvertType invertType);
	/**
	 * Common interface for returning the inversion state of a speed controller.
	 *
	 * @return isInverted The state of inversion, true is inverted.
	 */
	virtual bool GetInverted() const;
	//----------------------- turn-motor-off routines-------------------//
	/**
	 * Common interface for disabling a motor.
	 */
	virtual void Disable();
	/**
	 * Common interface to stop the motor until Set is called again.
	 */
	virtual void StopMotor() override;

	/**
	 * @return description of controller
	 */
	std::string GetDescription() const override;

  protected:
	/**
	 * Initialize sendable
	 * @param builder Base sendable to build on
	 */
	virtual void InitSendable(wpi::SendableBuilder &builder);

  private:
	double _speed = 0;
	std::string _desc;
};

} // namespace can
} // namespace motorcontrol
} // namespace phoenix
} // namespace ctre