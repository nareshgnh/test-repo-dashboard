// Fetch the list of reports from the Python server
function fetchReports() {
  fetch('/api/reports')
      .then(response => response.json())
      .then(data => {
          populateReportList(data);
      })
      .catch(error => console.error('Error fetching reports:', error));
}

// Populate the report list in the sidebar
function populateReportList(files) {
  const reportList = document.getElementById('reportList');
  reportList.innerHTML = '';  // Clear previous list

  // Reverse the files array to show the latest reports first
  files.reverse().forEach(file => {
      const listItem = document.createElement('li');
      
      // Add appropriate icon based on file type
      const icon = document.createElement('i');
      if (file.endsWith('.html')) {
          icon.className = 'fas fa-file-alt'; // Font Awesome HTML icon
      } else if (file.endsWith('.webm')) {
          icon.className = 'video-icon'; // Custom video icon
      }
      
      listItem.appendChild(icon);
      listItem.innerHTML += file;
      listItem.addEventListener('click', () => loadReport(file));
      reportList.appendChild(listItem);
  });
}

// Load the selected report into the iframe or video element
function loadReport(fileName) {
  const reportViewer = document.getElementById('reportViewer');
  const videoViewer = document.getElementById('videoViewer');
  
  if (fileName.endsWith('.html')) {
    reportViewer.src = `/reports/${fileName}`;
    reportViewer.style.display = 'block';
    videoViewer.style.display = 'none';
  } else if (fileName.endsWith('.webm')) {
    videoViewer.src = `/reports/${fileName}`;
    videoViewer.style.display = 'block';
    reportViewer.style.display = 'none';
  }
}

// Initialize the page by fetching the reports
fetchReports();
