/**
 * WPI Compliant Pigeon class.
 * WPILIB's object model requires many interfaces to be implemented to use
 * the various features.
 * This includes...
 * - LiveWindow/Test mode features
 * - getRotation2d/Gyro Interface
 * - Simulation Hooks
 */

#pragma once

#include "ctre/phoenix/sensors/PigeonIMU.h"
#include "ctre/phoenix/motorcontrol/can/TalonSRX.h"
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

#include "frc/interfaces/Gyro.h"
#include "frc/geometry/Rotation2d.h"
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

class WPI_PigeonIMU : public PigeonIMU,
                      public frc::Gyro,
                      public wpi::Sendable,
                      public wpi::SendableHelper<WPI_PigeonIMU> 
{
  public:
    /**
     * Construtor for WPI_PigeonIMU.
     * 
     * @param deviceNumber CAN Device ID of the Pigeon IMU.
     */
    WPI_PigeonIMU(int deviceNumber);
    /**
     * Construtor for WPI_PigeonIMU.
     * 
     * @param talon The Talon SRX ribbon-cabled to Pigeon.
     */
    WPI_PigeonIMU(ctre::phoenix::motorcontrol::can::TalonSRX& talon);

    ~WPI_PigeonIMU();
    
    WPI_PigeonIMU() = delete;
    WPI_PigeonIMU(WPI_PigeonIMU const &) = delete;
    WPI_PigeonIMU &operator=(WPI_PigeonIMU const &) = delete;

    void InitSendable(wpi::SendableBuilder& builder) override;

    void Calibrate() final {} //Pigeon doesn't need manual cal
    void Reset() final;
    double GetAngle() const override;
    double GetRate() const override;

    frc::Rotation2d GetRotation2d() const override;

  private:
    void Init();

    DeviceType m_simType;

    hal::SimDevice m_simPigeon;
	hal::SimDouble m_simFusedHeading;
	hal::SimDouble m_simRawHeading;

    static void OnValueChanged(const char* name, void* param, HAL_SimValueHandle handle,
							   HAL_Bool readonly, const struct HAL_Value* value);
	static void OnPeriodic(void* param);
};

} //namespace sensors
} //namespace phoenix
} //namespace ctre