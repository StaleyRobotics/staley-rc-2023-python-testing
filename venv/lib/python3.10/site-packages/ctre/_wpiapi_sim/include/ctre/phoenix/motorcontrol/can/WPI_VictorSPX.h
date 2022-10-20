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

#include "ctre/phoenix/motorcontrol/can/VictorSPX.h"
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
 * VEX Victor SPX Motor Controller when used on CAN Bus.
 */
class WPI_VictorSPX: public virtual VictorSPX,
					 public virtual WPI_BaseMotorController
{
public:
	/**
	 * Constructor for a WPI_VictorSPX
	 * @param deviceNumber Device ID of VictorSPX
	 */
	WPI_VictorSPX(int deviceNumber);
	virtual ~WPI_VictorSPX();

	WPI_VictorSPX() = delete;
	WPI_VictorSPX(WPI_VictorSPX const&) = delete;
	WPI_VictorSPX& operator=(WPI_VictorSPX const&) = delete;

	/* ----- virtual re-directs ------- */
	virtual void Set(double value);
	virtual void Set(ControlMode mode, double value);
	virtual void Set(ControlMode mode, double demand0, DemandType demand1Type, double demand1);
	virtual void Set(VictorSPXControlMode mode, double value);
	virtual void Set(VictorSPXControlMode mode, double demand0, DemandType demand1Type, double demand1);
	virtual void SetVoltage(units::volt_t output);
	virtual void SetInverted(InvertType invertType);
	virtual void SetInverted(bool bInvert);
	virtual ctre::phoenix::ErrorCode ConfigSelectedFeedbackSensor(RemoteFeedbackDevice feedbackDevice, int pidIdx = 0, int timeoutMs = 0);

protected:
	
private:

	hal::SimDevice m_simMotor;
	hal::SimDouble m_simPercOut;
	hal::SimDouble m_simMotorOutputLeadVoltage;
	hal::SimDouble m_simVbat;

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