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

#include "ctre/phoenix/motorcontrol/can/TalonSRX.h"
#include "ctre/phoenix/motorcontrol/can/WPI_BaseMotorController.h"
#include "ctre/phoenix/platform/Platform.h"
#include "ctre/phoenix/WPI_CallbackHelper.h"


//Turn off dominance warning
#if _MSC_VER
	#pragma warning(push)
	#pragma warning(disable : 4250)
#endif

using namespace ctre::phoenix;

namespace ctre {
namespace phoenix {
namespace motorcontrol {
namespace can {

/**
 * CTRE Talon SRX Motor Controller when used on CAN Bus.
 */
class WPI_TalonSRX : public virtual TalonSRX,
					 public virtual WPI_BaseMotorController
{
public:
	/**
	 * Constructor for a WPI_TalonSRX
	 * @param deviceNumber Device ID of TalonSRX
	 */
	WPI_TalonSRX(int deviceNumber);
	virtual ~WPI_TalonSRX();

	WPI_TalonSRX() = delete;
	WPI_TalonSRX(WPI_TalonSRX const &) = delete;
	WPI_TalonSRX &operator=(WPI_TalonSRX const &) = delete;

	/* ----- virtual re-directs ------- */
	virtual void Set(double value);
	virtual void Set(ControlMode mode, double value);
	virtual void Set(ControlMode mode, double demand0, DemandType demand1Type, double demand1);
	virtual void Set(TalonSRXControlMode mode, double value);
	virtual void Set(TalonSRXControlMode mode, double demand0, DemandType demand1Type, double demand1);
	virtual void SetVoltage(units::volt_t output);
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

	hal::SimDevice m_simAnalogEnc;
	hal::SimBoolean m_simAnalogInit;
	hal::SimDouble m_simAnalogVoltage;

	hal::SimDevice m_simPulseWidthEnc;
	hal::SimBoolean m_simPulseWidthConnected;
	hal::SimDouble m_simPulseWidthPos;

	hal::SimDevice m_simQuadEnc;
	hal::SimDouble m_simQuadPos;
	hal::SimDouble m_simQuadRawPos;
	hal::SimDouble m_simQuadVel;

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