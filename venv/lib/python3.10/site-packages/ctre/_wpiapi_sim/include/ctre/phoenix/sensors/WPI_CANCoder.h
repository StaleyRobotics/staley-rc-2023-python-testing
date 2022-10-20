/**
 * WPI Compliant CANcoder class.
 * WPILIB's object model requires many interfaces to be implemented to use
 * the various features.
 * This includes...
 * - LiveWindow/Test mode features
 * - Simulation Hooks
 */

#pragma once

#include "ctre/phoenix/sensors/CANCoder.h"
#include "ctre/phoenix/WPI_CallbackHelper.h"

#include <mutex>

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
#include "wpi/raw_ostream.h"
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
namespace sensors
{

class WPI_CANCoder : public CANCoder,
                     public wpi::Sendable,
					           public wpi::SendableHelper<WPI_CANCoder>
{
  public:
    /**
     * Construtor for CANCoder.
     *
     * @param deviceNumber CAN Device ID of the CANCoder.
	 * @param canbus Name of the CANbus; can be a CANivore device name or serial number.
	 *               Pass in nothing or "rio" to use the roboRIO.
     */
    WPI_CANCoder(int deviceNumber, std::string const &canbus = "");

    ~WPI_CANCoder();

    WPI_CANCoder() = delete;
    WPI_CANCoder(WPI_CANCoder const &) = delete;
    WPI_CANCoder &operator=(WPI_CANCoder const &) = delete;

    void InitSendable(wpi::SendableBuilder& builder) override;

  private:

	hal::SimDevice m_simCANCoder;
	hal::SimDouble m_simVbat;
	hal::SimDouble m_simPosition;
	hal::SimDouble m_simAbsPosition;
	hal::SimDouble m_simRawPosition;
	hal::SimDouble m_simVelocity;

  static void OnValueChanged(const char* name, void* param, HAL_SimValueHandle handle,
							   HAL_Bool readonly, const struct HAL_Value* value);
	static void OnPeriodic(void* param);
};

} //namespace sensors
} //namespace phoenix
} //namespace ctre