$locations = @(
    "Varberg, Sweden",
    "Malmö, Sweden",
    "Gothenburg, Sweden",
    "Stockholm Archipelago, Sweden",
    "Båstad, Sweden"
)

foreach ($i in 1..10) {
    foreach ($location in $locations) {
        $windSpeed = Get-Random -Minimum 8 -Maximum 25
        $temp = Get-Random -Minimum 15 -Maximum 22
        $waveHeight = Get-Random -Minimum 0.5 -Maximum 2.5
        $directions = @("N", "NE", "E", "SE", "S", "SW", "W", "NW")
        $windDir = Get-Random -InputObject $directions

        $body = @{
            location = $location
            wind_speed = [math]::Round($windSpeed, 1)
            wind_direction = $windDir
            temperature = [math]::Round($temp, 1)
            wave_height = [math]::Round($waveHeight, 1)
        } | ConvertTo-Json

        Invoke-WebRequest -Uri "http://localhost:8000/weather-data/" -Method Post -ContentType "application/json" -Body $body
        Start-Sleep -Milliseconds 500
    }
}
