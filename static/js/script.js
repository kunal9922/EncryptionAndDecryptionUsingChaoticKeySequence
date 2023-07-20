document.addEventListener("DOMContentLoaded", function () {
  /*This JavaScript code enables the encryption and decryption of 
  images using the provided forms and communicates with the corresponding 
  Flask endpoints on the server side. */
  const encryptForm = document.getElementById("encryptForm");
  encryptForm.addEventListener("submit", async function (event) {
    event.preventDefault();

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
      }
    };

    reader.readAsDataURL(encryptedImageFile);
  });
});