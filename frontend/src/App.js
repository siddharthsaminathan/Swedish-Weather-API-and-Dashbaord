import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Typography, 
  Paper, 
  Grid,
  Card,
  CardContent,
} from '@mui/material';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import axios from 'axios';

function App() {
  const [weatherData, setWeatherData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/weather-data/');
        setWeatherData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 30000); // Refresh every 30 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h3" component="h1" gutterBottom>
        WindSurf Analytics Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* Wind Speed Chart */}
        <Grid item xs={12}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Wind Speed Over Time
            </Typography>
            <LineChart
              width={1000}
              height={300}
              data={weatherData}
              margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="timestamp" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="wind_speed" stroke="#8884d8" />
            </LineChart>
          </Paper>
        </Grid>

        {/* Current Conditions */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Current Conditions
              </Typography>
              {weatherData[0] && (
                <>
                  <Typography variant="body1">
                    Location: {weatherData[0].location}
                  </Typography>
                  <Typography variant="body1">
                    Wind Speed: {weatherData[0].wind_speed} knots
                  </Typography>
                  <Typography variant="body1">
                    Wind Direction: {weatherData[0].wind_direction}
                  </Typography>
                  <Typography variant="body1">
                    Temperature: {weatherData[0].temperature}°C
                  </Typography>
                  <Typography variant="body1">
                    Wave Height: {weatherData[0].wave_height}m
                  </Typography>
                </>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
