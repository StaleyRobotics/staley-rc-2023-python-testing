#pragma once

#include "hal/simulation/SimDeviceData.h"
#include "hal/simulation/MockHooks.h"
#include "ctre/phoenix/cci/Platform_CCI.h"
#include <hal/SimDevice.h>

namespace ctre
{
namespace phoenix
{
    class WPI_CallbackHelper {
    public:
        static double GetRawValue(const HAL_Value* value) {
            switch(value->type) {
            case HAL_DOUBLE:
                return value->data.v_double;
            case HAL_BOOLEAN:
                return value->data.v_boolean;
            case HAL_INT:
                return value->data.v_int;
            case HAL_LONG:
                return value->data.v_long;
            case HAL_ENUM:
                return value->data.v_enum;
            default:
                return 0;
            }
        }
    };
} //namespace phoenix
} //namespace ctre