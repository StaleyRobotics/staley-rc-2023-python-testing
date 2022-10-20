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

#include "ctre/phoenix/sensors/Pigeon2.h"
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

class WPI_Pigeon2 : public Pigeon2,
                    public frc::Gyro,
                    public wpi::Sendable,
                    public wpi::SendableHelper<WPI_Pigeon2>
{
  public:
    /**
     * Construtor for WPI_Pigeon2.
     * 
     * @param deviceNumber CAN Device ID of the Pigeon 2.
     * @param canbus Name of the CANbus; can be a CANivore device name or serial number.
     *               Pass in nothing or "rio" to use the roboRIO.
     */
    WPI_Pigeon2(int deviceNumber, std::string const &canbus = "");

    ~WPI_Pigeon2();
    
    WPI_Pigeon2() = delete;
    WPI_Pigeon2(WPI_Pigeon2 const &) = delete;
    WPI_Pigeon2 &operator=(WPI_Pigeon2 const &) = delete;

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
    hal::SimDouble m_simYaw;
    hal::SimDouble m_simRawYaw;

    static void OnValueChanged(const char* name, void* param, HAL_SimValueHandle handle,
                               HAL_Bool readonly, const struct HAL_Value* value);
    static void OnPeriodic(void* param);
};

} //namespace sensors
} //namespace phoenix
} //namespace ctre