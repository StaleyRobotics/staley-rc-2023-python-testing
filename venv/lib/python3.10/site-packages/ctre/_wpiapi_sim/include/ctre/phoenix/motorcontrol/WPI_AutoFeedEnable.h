#pragma once

#include "frc/DriverStation.h"
#include "ctre/phoenix/unmanaged/Unmanaged.h"
#include "hal/simulation/MockHooks.h"

namespace ctre {
namespace phoenix {
namespace motorcontrol {
    class WPI_AutoFeedEnable {
    public:
        static WPI_AutoFeedEnable& GetInstance() {
            static WPI_AutoFeedEnable* autoFeedEnable = new WPI_AutoFeedEnable();
            return *autoFeedEnable;
        }

    private:
        WPI_AutoFeedEnable() {
            HALSIM_RegisterSimPeriodicBeforeCallback(OnPeriodic, this);
        }

        static void OnPeriodic(void* param) {
            if (frc::DriverStation::GetInstance().IsEnabled()) {
                unmanaged::Unmanaged::FeedEnable(100);
            }
        }
    };
}
}
}