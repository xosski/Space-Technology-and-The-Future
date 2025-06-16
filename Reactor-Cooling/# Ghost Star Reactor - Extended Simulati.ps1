# Ghost Star Reactor - Extended Simulation with Phantasmal Sheath Monitoring

# Core variables
$ReactorPowerMW = 1000
$TPVEfficiency = 0.35
$PhotonThrustPerMW = 0.03
$IonBurstPowerReserve = 100
$PhotonDriveActive = $true
$SCRAM = $false

# Phantasmal Sheath variables
$LatticeIntegrity = 100           # %
$HarmonicSyncDelta = 2.0          # ms
$CryoJacketPressure = 3.2         # atm
$SheathState = "Stable"

function Initialize-System {
    Write-Host "Initializing Ghost Star Reactor simulation..."
    $Global:PhotonThrust = $ReactorPowerMW * $TPVEfficiency * $PhotonThrustPerMW
    $Global:ElectricOutputMW = $ReactorPowerMW * $TPVEfficiency
    $Global:BackupHeatMW = $ReactorPowerMW - $ElectricOutputMW
    $Global:SystemState = "Startup"
}

function Start-Reactor {
    Write-Host "Starting reactor..."
    Start-Sleep -Seconds 2
    $Global:SystemState = "Normal"
    Write-Host "Reactor online. Current power output: $ReactorPowerMW MW"
    Monitor-Sheath
}

function Run-NormalOperation {
    Write-Host "Running normal operations..."
    Write-Host "Electric output: $ElectricOutputMW MW"
    Write-Host "Photon drive thrust: $PhotonThrust N"
    Write-Host "Heat routed to backup loop: $BackupHeatMW MW"
    Degrade-Sheath
    Monitor-Sheath
}

function SCRAM-Reactor {
    Write-Host "SCRAM initiated! Shutting down reactor immediately..."
    $Global:ReactorPowerMW = 0
    $Global:ElectricOutputMW = 0
    $Global:PhotonThrust = 0
    $Global:SystemState = "SCRAM"
    $PhotonDriveActive = $false
    Write-Host "Reactor is offline."
    Monitor-Sheath
}

function Emergency-Maneuver {
    param([float]$DeltaV, [string]$Vector)
    Write-Host "Emergency trajectory correction detected."
    if ($ElectricOutputMW - $IonBurstPowerReserve - 50 -lt 0) {
        Write-Host "Insufficient power to perform maneuver safely."
    }
    else {
        $ThrustRequired = $DeltaV * 0.1
        Write-Host "Firing ion engines towards $Vector with delta-V of $DeltaV m/s (est. thrust: $ThrustRequired N)"
    }
    Degrade-Sheath
    Monitor-Sheath
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

function Degrade-Sheath {
    $global:LatticeIntegrity -= Get-Random -Minimum 1 -Maximum 3
    $global:HarmonicSyncDelta += Get-Random -Minimum 0.1 -Maximum 0.4
    $global:CryoJacketPressure -= Get-Random -Minimum 0.01 -Maximum 0.03
}

function Monitor-Sheath {
    if ($LatticeIntegrity -lt 60 -and $CryoJacketPressure -lt 3.0) {
        $SheathState = "Critical"
        Write-Host "[ALERT] Lattice Collapse Conditions Detected (LC-7). Retreat and engage cryojet!"
    }
    elseif ($HarmonicSyncDelta -gt 3.5) {
        $SheathState = "Warning"
        Write-Host "[WARNING] Harmonic sync drift exceeding 3.5ms!"
    }
    else {
        $SheathState = "Stable"
    }
    Write-Host "Sheath Status → Integrity: $LatticeIntegrity%, Sync Drift: $HarmonicSyncDelta ms, Cryo Pressure: $CryoJacketPressure atm, State: $SheathState"
}

# Main simulation
Initialize-System
Start-Reactor
Run-NormalOperation
Start-Sleep -Seconds 2
Emergency-Maneuver -DeltaV 20 -Vector "Port"
Start-Sleep -Seconds 2
SCRAM-Reactor
Start-Sleep -Seconds 2
Shutdown-Reactor
