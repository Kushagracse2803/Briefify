const summarizeBtn = document.getElementById('summarizeBtn');
const inputText = document.getElementById('input-text');
const outputArea = document.getElementById('output-area');
const summarySlider = document.getElementById('summarySlider');

const uploadForm = document.getElementById('uploadForm');
const fileInput = document.getElementById('fileInput');
const fileNameDisplay = document.getElementById('fileNameDisplay');
const pasteBtn = document.getElementById('pasteBtn'); // Assuming this exists in HTML

let selectedFile = null;

// Summarize button click handler
summarizeBtn.addEventListener('click', async () => {
  const text = inputText.value.trim();
  if (!text) {
    outputArea.textContent = "Please enter some text to summarize.";
    return;
  }

  const lengthMap = { '1': 'short', '2': 'medium', '3': 'long' };
  const selectedLength = lengthMap[summarySlider.value];

  summarizeBtn.disabled = true;
  outputArea.textContent = "Summarizing... Please wait.";

  try {
    const response = await fetch('/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text, length: selectedLength }),
    });

    const data = await response.json();
    outputArea.textContent = data.summary || "No summary returned.";
  } catch (error) {
    outputArea.textContent = "Error generating summary.";
    console.error(error);
  } finally {
    summarizeBtn.disabled = false;
  }
});

// File input change handler: show file name, clear texts, enable paste btn
fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    selectedFile = fileInput.files[0];
    fileNameDisplay.textContent = selectedFile.name;
    inputText.value = "";
    outputArea.textContent = "";
    if (pasteBtn) pasteBtn.disabled = false;
  } else {
    selectedFile = null;
    fileNameDisplay.textContent = "";
    if (pasteBtn) pasteBtn.disabled = true;
  }
});

// Upload button triggers file input click
const uploadBtn = document.getElementById('uploadBtn');
uploadBtn.addEventListener('click', () => {
  fileInput.click();
});

// Paste Extracted Text button handler: upload file and paste extracted text
if (pasteBtn) {
  pasteBtn.addEventListener('click', async () => {
    if (!selectedFile) {
      alert("Please select a file first.");
      return;
    }

    inputText.value = "";
    outputArea.textContent = "";
    pasteBtn.disabled = true;
    pasteBtn.textContent = "Extracting...";

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();

      if (data.extracted_text) {
        inputText.value = data.extracted_text;
      } else if (data.error) {
        alert(data.error);
      }
    } catch (error) {
      alert("Error uploading file.");
      console.error(error);
    } finally {
      pasteBtn.disabled = false;
      pasteBtn.textContent = "Paste Extracted Text";
      // Optionally reset file input and filename for fresh upload next time
      fileInput.value = "";
      fileNameDisplay.textContent = "";
      selectedFile = null;
      pasteBtn.disabled = true;
    }
  });
}
