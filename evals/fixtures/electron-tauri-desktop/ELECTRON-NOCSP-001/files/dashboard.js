window.electronAPI.onDashboardUpdate((payload) => {
  document.getElementById("dashboard").textContent = payload.summary;
});
