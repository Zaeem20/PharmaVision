document
        .getElementById("openDialogBtn")
        .addEventListener("click", openDialog);

      function openDialog() {
        document.getElementById("dialog").style.display = "block";
      }

      function closeDialog() {
        document.getElementById("dialog").style.display = "none";
      }
      document.getElementById('uploadBtn').addEventListener('click', function() {
        var fileInput = document.getElementById('fileInput');
        
        // Check if a file is selected
        if (fileInput.files.length > 0) {
          var selectedFile = fileInput.files[0];
          alert('File selected: ' + selectedFile.name);
          // You can perform further actions, such as uploading the file to a server, here.
        } else {
          alert('Please choose a file before clicking Upload.');
        }
      });