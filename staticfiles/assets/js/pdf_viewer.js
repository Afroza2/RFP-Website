// static/js/pdf_viewer.js

document.addEventListener('DOMContentLoaded', function() {
    // Select all PDF preview containers
    var pdfContainers = document.querySelectorAll('.pdf-preview-container');

    // Loop through each container
    pdfContainers.forEach(function(container) {
        // Get the PDF URL from data attribute
        var pdfUrl = container.getAttribute('data-pdf-url');

        // Create a new PDF.js viewer
        var pdfViewer = document.createElement('iframe');
        pdfViewer.src = 'https://mozilla.github.io/pdf.js/web/viewer.html?file=' + encodeURIComponent(pdfUrl);
        pdfViewer.width = '100%';
        pdfViewer.height = '400px'; // Set the desired height

        // Append the viewer to the container
        container.appendChild(pdfViewer);
    });
});
