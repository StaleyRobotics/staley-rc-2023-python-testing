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

#include "ctre/phoenix/motorcontrol/can/TalonFX.h"
#include "ctre/phoenix/motorcontrol/can/WPI_BaseMotorController.h"
#include "ctre/phoenix/platform/Platform.h"
#include "ctre/phoenix/WPI_CallbackHelper.h"


//Turn off dominance warning
#if _MSC_VER
	#pragma warning(push)
	#pragma warning(disable : 4250)
#endif

namespace ctre {
namespace phoenix {
namespace motorcontrol {
namespace can {

/**
 * CTRE Talon FX Motor Controller when used on CAN Bus.
 */
class WPI_TalonFX : public virtual TalonFX,
					 public virtual WPI_BaseMotorController
{
public:
	/**
	 * Constructor for a WPI_TalonFX
	 * @param deviceNumber Device ID of TalonFX
	 * @param canbus Name of the CANbus; can be a CANivore device name or serial number.
	 *               Pass in nothing or "rio" to use the roboRIO.
	 */
	WPI_TalonFX(int deviceNumber, std::string const &canbus = "");
	virtual ~WPI_TalonFX();

	WPI_TalonFX() = delete;
	WPI_TalonFX(WPI_TalonFX const &) = delete;
	WPI_TalonFX &operator=(WPI_TalonFX const &) = delete;

	/* ----- virtual re-directs ------- */
	virtual void Set(double value);
	virtual void Set(ControlMode mode, double value);
	virtual void Set(ControlMode mode, double demand0, DemandType demand1Type, double demand1);
	virtual void Set(TalonFXControlMode mode, double value);
	virtual void Set(TalonFXControlMode mode, double demand0, DemandType demand1Type, double demand1);
	virtual void SetVoltage(units::volt_t output);
	virtual void SetInverted(TalonFXInvertType invertType);
	virtual void SetInverted(InvertType invertType);
	virtual void SetInverted(bool bInvert);
	virtual ctre::phoenix::ErrorCode ConfigSelectedFeedbackSensor(FeedbackDevice feedbackDevice, int pidIdx = 0, int timeoutMs = 0);
	virtual ctre::phoenix::ErrorCode ConfigSelectedFeedbackSensor(RemoteFeedbackDevice feedbackDevice, int pidIdx = 0, int timeoutMs = 0);

protected:

private:

	hal::SimDevice m_simMotor;
	hal::SimDouble m_simPercOut;
	hal::SimDouble m_simMotorOutputLeadVoltage;
	hal::SimDouble m_simSupplyCurrent;
	hal::SimDouble m_simMotorCurrent;
	hal::SimDouble m_simVbat;

	hal::SimDevice m_simIntegSens;
	hal::SimDouble m_simIntegSensPos;
	hal::SimDouble m_simIntegSensAbsPos;
	hal::SimDouble m_simIntegSensRawPos;
	hal::SimDouble m_simIntegSensVel;

	hal::SimDevice m_simFwdLim;
	hal::SimBoolean m_simFwdLimInit;
	hal::SimBoolean m_simFwdLimInput;
	hal::SimBoolean m_simFwdLimValue;

	hal::SimDevice m_simRevLim;
	hal::SimBoolean m_simRevLimInit;
	hal::SimBoolean m_simRevLimInput;
	hal::SimBoolean m_simRevLimValue;

	static void OnValueChanged(const char* name, void* param, HAL_SimValueHandle handle,
							   HAL_Bool readonly, const struct HAL_Value* value);
	static void OnPeriodic(void* param);

};

} // namespace can
} // namespace motorcontrol
} // namespace phoenix
} // namespace ctre

#if _MSC_VER
	#pragma warning(pop)
#endif