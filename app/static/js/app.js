const form = document.getElementById("weather-form");
const cityInput = document.getElementById("city");
const statusEl = document.getElementById("status");
const currentCard = document.getElementById("current-card");
const forecastCard = document.getElementById("forecast-card");
const currentTitle = document.getElementById("current-title");
const currentMetrics = document.getElementById("current-metrics");
const forecastList = document.getElementById("forecast-list");

function setStatus(message, type = "") {
  statusEl.textContent = message;
  statusEl.className = `status ${type}`.trim();
}

function toValue(value, suffix = "") {
  if (value === null || value === undefined || value === "") {
    return "-";
  }
  return `${value}${suffix}`;
}

function renderCurrent(city, data) {
  const current = data.currentConditions || {};
  currentTitle.textContent = `Current Conditions - ${city}`;

  const items = [
    ["Temperature", toValue(current.temp, " C")],
    ["Feels Like", toValue(current.feelslike, " C")],
    ["Humidity", toValue(current.humidity, " %")],
    ["Wind", toValue(current.windspeed, " km/h")],
    ["Condition", toValue(current.conditions)],
    ["Cloud Cover", toValue(current.cloudcover, " %")],
  ];

  currentMetrics.innerHTML = items
    .map(
      ([label, value]) =>
        `<article class="metric"><span class="metric-label">${label}</span><span class="metric-value">${value}</span></article>`
    )
    .join("");

  currentCard.classList.remove("hidden");
}

function renderForecast(data) {
  const days = (data.days || []).slice(0, 7);

  if (!days.length) {
    forecastCard.classList.add("hidden");
    return;
  }

  forecastList.innerHTML = days
    .map((day) => {
      return `<article class="forecast-item">
        <strong>${toValue(day.datetime)}</strong>
        <span>Min ${toValue(day.tempmin, " C")}</span>
        <span>Max ${toValue(day.tempmax, " C")}</span>
      </article>`;
    })
    .join("");

  forecastCard.classList.remove("hidden");
}

async function fetchWeather(city) {
  const response = await fetch(`/weather?city=${encodeURIComponent(city)}`);
  const data = await response.json();

  if (!response.ok) {
    const message = data.error || "Failed to fetch weather data.";
    throw new Error(message);
  }

  return data;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const city = cityInput.value.trim();

  if (!city) {
    setStatus("Please enter a city.", "error");
    return;
  }

  setStatus("Loading weather data...");
  currentCard.classList.add("hidden");
  forecastCard.classList.add("hidden");

  try {
    const data = await fetchWeather(city);
    renderCurrent(city, data);
    renderForecast(data);
    setStatus("Weather loaded successfully.", "ok");
  } catch (error) {
    setStatus(error.message, "error");
  }
});
