
# Ghost Star Reactor - Optimal Conditions Space Travel Simulation
# Simulates: Reactor startup, normal operation, SCRAM, emergency trajectory correction

# Initialize global variables
$ReactorPowerMW = 1000           # Total reactor power in MW
$TPVEfficiency = 0.35            # TPV conversion efficiency
$PhotonThrustPerMW = 0.03        # Thrust per MW (N)
$IonBurstPowerReserve = 100      # MW reserved for ion bursts
$PhotonDriveActive = $true
$SCRAM = $false

function Initialize-System {
    Write-Host "Initializing Ghost Star Reactor simulation..."
    $Global:PhotonThrust = $ReactorPowerMW * $TPVEfficiency * $PhotonThrustPerMW
    $Global:ElectricOutputMW = $ReactorPowerMW * $TPVEfficiency
    $Global:BackupHeatMW = $ReactorPowerMW - $ElectricOutputMW
    $Global:SystemState = "Startup"
}

function Start-Reactor {
    Write-Host "Starting reactor..."
    Start-Sleep -Seconds 5
    $Global:SystemState = "Normal"
    Write-Host "Reactor online. Current power output: $ReactorPowerMW MW"
}

function Run-NormalOperation {
    Write-Host "Running normal operations..."
    Write-Host "Electric output: $ElectricOutputMW MW"
    Write-Host "Photon drive thrust: $PhotonThrust N"
    Write-Host "Heat routed to backup loop: $BackupHeatMW MW"
}

function SCRAM-Reactor {
    Write-Host "SCRAM initiated! Shutting down reactor immediately..."
    $Global:ReactorPowerMW = 0
    $Global:ElectricOutputMW = 0
    $Global:PhotonThrust = 0
    $Global:SystemState = "SCRAM"
}

function Emergency-Maneuver {
    param([float]$DeltaV, [string]$Vector)
    Write-Host "Emergency trajectory correction detected."
    if ($ElectricOutputMW - $IonBurstPowerReserve - 50 -lt 0) {
        Write-Host "Insufficient power to perform maneuver safely."
    } else {
        $ThrustRequired = $DeltaV * 0.1  # Simplified force conversion
        Write-Host "Firing ion engines towards $Vector with delta-V of $DeltaV m/s (est. thrust: $ThrustRequired N)"
    }
}

function Shutdown-Reactor {
    Write-Host "Powering down reactor safely..."
    $Global:SystemState = "Shutdown"
    $Global:PhotonDriveActive = $false
    $Global:ReactorPowerMW = 0
    $Global:ElectricOutputMW = 0
    $Global:PhotonThrust = 0
    Write-Host "System shutdown complete."
}

# Main simulation
Initialize-System
Start-Reactor
Run-NormalOperation

# Simulate emergency
Start-Sleep -Seconds 3
Emergency-Maneuver -DeltaV 20 -Vector "Port"

# Simulate reactor scram
Start-Sleep -Seconds 2
SCRAM-Reactor

# Final safe shutdown
Start-Sleep -Seconds 2
Shutdown-Reactor
