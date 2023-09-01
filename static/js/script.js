document.addEventListener("DOMContentLoaded", function () {
// Get the loading overlay element
const loadingOverlay = document.getElementById("loadingOverlay");


  // Get the encryption and decryption drop containers and file inputs
  const encryptDropContainer = document.getElementById('encrypt-drop-container'); // Remove the dot before class name
  const decryptDropContainer = document.getElementById('decrypt-drop-container'); // Remove the dot before class name
  const encryptFileInput = document.getElementById('image');
  const decryptFileInput = document.getElementById('encryptedImageFile');

  // Function to handle highlighting of drop containers
  function highlightDropContainer(dropContainer) {
    dropContainer.classList.add('highlight');
  }

  // Function to handle removing highlight from drop containers
  function unhighlightDropContainer(dropContainer) {
    dropContainer.classList.remove('highlight');
  }
  encryptDropContainer.addEventListener('dragover', (e) => {
    e.preventDefault();
  });

  decryptDropContainer.addEventListener('dragover', (e) => {
    e.preventDefault();
  });

  encryptDropContainer.addEventListener('drop', (e) => {
    e.preventDefault();
    encryptDropContainer.classList.remove('highlight'); // Remove the highlight class

    const files = e.dataTransfer.files;
    encryptFileInput.files = files;
    handleFiles(files, "image");
});

decryptDropContainer.addEventListener('drop', (e) => {
  e.preventDefault();
  decryptDropContainer.classList.remove('highlight'); // Remove the highlight class

  const files = e.dataTransfer.files;
  decryptFileInput.files = files;
  handleFiles(files, "encryptedImageFile");
});
  // // Add event listeners for dragging over the encryption file input
  // encryptFileInput.addEventListener('dragenter', () => {
  //   highlightDropContainer(encryptDropContainer);
  // });

  // encryptFileInput.addEventListener('dragleave', () => {
  //   unhighlightDropContainer(encryptDropContainer);
  // });

  // // Add event listeners for dragging over the decryption file input
  // decryptFileInput.addEventListener('dragenter', () => {
  //   highlightDropContainer(decryptDropContainer);
  // });

  // decryptFileInput.addEventListener('dragleave', () => {
  //   unhighlightDropContainer(decryptDropContainer);
  // });

  // Prevent default behavior to enable drop
 
  // Handle file input change
  encryptFileInput.addEventListener('change', (event) => { // Change 'fileInput' to 'encryptFileInput'
    const files = event.target.files;
    console.log(event.target.id)
    handleFiles(files, event.target.id);
  });

  decryptFileInput.addEventListener('change', (event) => { // Change 'fileInput' to 'decryptFileInput'
    const files = event.target.files;
    console.log(event.target.id)
    handleFiles(files, event.target.id);
  });
// Function to remove existing image from a container
function removeImage(container) {
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}
  // Store file names in an array
  const fileNames = [];

  // Get the image preview element
  const imagePreviewEn = document.querySelector('#image-preview-en'); // Make sure you have an element with class 'image-preview'
  const imagePreviewDe = document.querySelector('#image-preview-de'); // Make sure you have an element with class 'image-preview'
  // Handle dropped or selected files for encryption and decryption
  function handleFiles(files, targetId) {
    for (const file of files) {
      if (file.type.startsWith('image/')) {
        if (targetId === 'image') {
          const imgContainerEn = document.createElement('div');
          imgContainerEn.classList.add('image-container');

          const img = document.createElement('img');
          img.src = URL.createObjectURL(file);
          imgContainerEn.appendChild(img);

          const fileNameE = document.createElement('p');
          fileNameE.textContent = file.name;
          imgContainerEn.appendChild(fileNameE);

          fileNames.push(file.name); // Store the file name
          // updateImageFilenamesInput(); // Update the input field with file names
          removeImage(imagePreviewEn); // Remove existing image, if any
        imagePreviewEn.appendChild(imgContainerEn);

        } else if (targetId === 'encryptedImageFile') {
          const imgContainerDe = document.createElement('div');
        imgContainerDe.classList.add('image-container');

        const img = document.createElement('img');
        img.src = URL.createObjectURL(file);
        imgContainerDe.appendChild(img);

        const fileName = document.createElement('p');
        fileName.textContent = file.name;
        imgContainerDe.appendChild(fileName);

        fileNames.push(file.name); // Store the file name
        // updateImageFilenamesInput(); // Update the input field with file names
        removeImage(imagePreviewDe); // Remove existing image, if any
        imagePreviewDe.appendChild(imgContainerDe);
        }
      }
    }
  }

  // Show the loading overlay
  function showLoadingOverlay() {
    loadingOverlay.style.display = "flex";
  }

  // Hide the loading overlay
  function hideLoadingOverlay() {
    loadingOverlay.style.display = "none";
  }

  /*This JavaScript code enables the encryption and decryption of 
  images using the provided forms and communicates with the corresponding 
  Flask endpoints on the server side. */
  const encryptForm = document.getElementById("encryptForm");
  encryptForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    showLoadingOverlay(); // Show the loading overlay before starting the encryption process

    const initCond = parseFloat(document.getElementById("initCond").value);
    const controlPara = parseFloat(document.getElementById("controlPara").value);
    const image = document.getElementById("image").files[0];

    const reader = new FileReader();
    reader.onload = async function (e) {
      const imgData = e.target.result.split(",")[1];
      const requestData = {
        initCond: initCond,
        controlPara: controlPara,
        image: imgData,
      };

      try {
        const response = await fetch("/encrypt", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestData),
        });
        const data = await response.json();

        const encryptedImage = document.getElementById("encryptedImage");
        encryptedImage.innerHTML = `<img src="data:image/jpeg;base64, ${data.encryptedImage}" alt="Encrypted Image">`;

        // Create a new image element for the bifurcation diagram
        const bifurcationImage = document.createElement("img");
        bifurcationImage.src = `data:image/png;base64, ${data.bifurcationImage}`;
        bifurcationImage.alt = "Bifurcation Diagram";

        // Add the bifurcation diagram image to the bifurcationContainer
        const bifurcationContainer = document.getElementById("bifurcationDiagramEn");
        bifurcationContainer.innerHTML = "";
        bifurcationContainer.appendChild(bifurcationImage);
      } catch (error) {
        console.error(error);
      }finally {
        hideLoadingOverlay(); // Hide the loading overlay after the encryption process is complete
      }
    };

    reader.readAsDataURL(image);
  });
    // Get the download button element
    const downloadButton = document.getElementById("downloadEncrypted");

    // Add an event listener to the download button
    downloadButton.addEventListener("click", async function () {
      try {
        // Fetch the encrypted image file from the server
        const downloadResponse = await fetch("/download_encrypted");
        const blob = await downloadResponse.blob();

        // Create a URL for the blob data
        const url = URL.createObjectURL(blob);

        // Create an anchor element with the encrypted image URL
        const downloadLink = document.createElement("a");
        downloadLink.href = url;
        downloadLink.download = "encrypted_image.jpg"; // Set the filename for download
        downloadLink.style.display = "none";

        // Append the download link to the document body
        document.body.appendChild(downloadLink);

        // Click the download link to trigger the download
        downloadLink.click();

        // Remove the download link from the document body
        document.body.removeChild(downloadLink);

        // Revoke the object URL to free up resources
        URL.revokeObjectURL(url);
      } catch (error) {
        console.error(error);
      }
    });
  const decryptForm = document.getElementById("decryptForm");

  decryptForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    showLoadingOverlay(); // Show the loading overlay before starting the decryption process

    const decryptInitCond = parseFloat(document.getElementById("decryptInitCond").value);
    const decryptControlPara = parseFloat(document.getElementById("decryptControlPara").value);
    const encryptedImageFile = document.getElementById("encryptedImageFile").files[0];

    const reader = new FileReader();
    reader.onload = async function (e) {
      const encryptedImageData = e.target.result.split(",")[1];
      const requestData = {
        initCond: decryptInitCond,
        controlPara: decryptControlPara,
        encryptedImage: encryptedImageData,
      };

      try {
        const response = await fetch("/decrypt", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestData),
        });
        const data = await response.json();

        const decryptedImage = document.getElementById("decryptedImage");
        decryptedImage.innerHTML = `<img src="data:image/jpeg;base64, ${data.decryptedImage}" alt="Decrypted Image">`;

        // Create a new image element for the bifurcation diagram
        const bifurcationImage = document.createElement("img");
        bifurcationImage.src = `data:image/png;base64, ${data.bifurcationImage}`;
        bifurcationImage.alt = "Bifurcation Diagram";

        // Add the bifurcation diagram image to the bifurcationContainer
        const bifurcationContainer = document.getElementById("bifurcationDiagramDe");
        bifurcationContainer.innerHTML = "";
        bifurcationContainer.appendChild(bifurcationImage);
      } catch (error) {
        console.error(error);
      } finally {
        hideLoadingOverlay(); // Hide the loading overlay after the decryption process is complete
      }
    };

    reader.readAsDataURL(encryptedImageFile);
  });
  // Get the download button element
  const downloadButtonDe = document.getElementById("downloadDecrypted");

  // Add an event listener to the download button
  downloadButtonDe.addEventListener("click", async function () {
    try {
      // Fetch the encrypted image file from the server
      const downloadResponse = await fetch("/download_decrypted");
      const blob = await downloadResponse.blob();

      // Create a URL for the blob data
      const url = URL.createObjectURL(blob);

      // Create an anchor element with the encrypted image URL
      const downloadLink = document.createElement("a");
      downloadLink.href = url;
      downloadLink.download = "decrypted_image.jpg"; // Set the filename for download
      downloadLink.style.display = "none";

      // Append the download link to the document body
      document.body.appendChild(downloadLink);

      // Click the download link to trigger the download
      downloadLink.click();

      // Remove the download link from the document body
      document.body.removeChild(downloadLink);

      // Revoke the object URL to free up resources
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error(error);
    }
  });
});