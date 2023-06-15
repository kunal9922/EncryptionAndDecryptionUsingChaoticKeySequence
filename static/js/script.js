document.addEventListener("DOMContentLoaded", function () {
    const encryptForm = document.getElementById("encryptForm");
    encryptForm.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const initCond = parseFloat(document.getElementById("initCond").value);
      const controlPara = parseFloat(document.getElementById("controlPara").value);
      const image = document.getElementById("image").files[0];
  
      const reader = new FileReader();
      reader.onload = function (e) {
        const imgData = e.target.result.split(",")[1];
        const requestData = {
          initCond: initCond,
          controlPara: controlPara,
          image: imgData,
        };
  
        fetch("/encrypt", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestData),
        })
          .then((response) => response.json())
          .then((data) => {
            const encryptedImage = document.getElementById("encryptedImage");
            encryptedImage.innerHTML = `<img src="data:image/jpeg;base64, ${data.encryptedImage}" alt="Encrypted Image">`;
          })
          .catch((error) => console.error(error));
      };
  
      reader.readAsDataURL(image);
    });
  
    const decryptForm = document.getElementById("decryptForm");
    decryptForm.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const decryptInitCond = parseFloat(
        document.getElementById("decryptInitCond").value
      );
      const decryptControlPara = parseFloat(
        document.getElementById("decryptControlPara").value
      );
      const encryptedImageFile = document.getElementById("encryptedImageFile")
        .files[0];
  
      const reader = new FileReader();
      reader.onload = function (e) {
        const encryptedImageData = e.target.result.split(",")[1];
        const requestData = {
          initCond: decryptInitCond,
          controlPara: decryptControlPara,
          encryptedImage: encryptedImageData,
        };
  
        fetch("/decrypt", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestData),
        })
          .then((response) => response.json())
          .then((data) => {
            const decryptedImage = document.getElementById("decryptedImage");
            decryptedImage.innerHTML = `<img src="data:image/jpeg;base64, ${data.decryptedImage}" alt="Decrypted Image">`;
          })
          .catch((error) => console.error(error));
      };
  
      reader.readAsDataURL(encryptedImageFile);
    });
  });
  