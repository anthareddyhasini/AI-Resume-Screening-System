const resumeInput =
document.getElementById('resumeFile');

const fileName =
document.getElementById('fileName');

const progressBar =
document.getElementById('progressBar');


// Resume File Preview + Progress Bar

resumeInput.addEventListener('change', function () {

    if (resumeInput.files.length > 0) {

        fileName.textContent =
        "Selected File: " +
        resumeInput.files[0].name;

        let width = 0;

        let interval =
        setInterval(function(){

            if(width >= 100){

                clearInterval(interval);

            }
            else{

                width++;

                progressBar.style.width =
                width + "%";

            }

        },15);

    }

    else {

        fileName.textContent =
        "No file selected";

        progressBar.style.width = "0%";

    }

});


// Auto Fill Job Description

function fillJobDescription(){

    const role =
    document.getElementById(
    "jobRole"
    ).value;

    const textarea =
    document.getElementById(
    "jobDescription"
    );

    if(role === "python"){

        textarea.value =
        "Looking for Python Developer with Python, Flask, SQL, APIs and problem solving skills.";

    }

    else if(role === "frontend"){

        textarea.value =
        "Looking for Frontend Developer with HTML, CSS, JavaScript and React skills.";

    }

    else if(role === "datascience"){

        textarea.value =
        "Looking for Data Scientist with Python, Machine Learning and Data Analysis skills.";

    }

    else if(role === "aiml"){

        textarea.value =
        "Looking for AI/ML Engineer with NLP, Deep Learning and Machine Learning skills.";

    }

    else if(role === "doctor"){

        textarea.value =
        "Looking for Doctor with diagnosis, patient care and medical expertise.";

    }

    else if(role === "teacher"){

        textarea.value =
        "Looking for Teacher with communication, classroom management and subject expertise.";

    }

    else if(role === "accountant"){

        textarea.value =
        "Looking for Accountant with GST and bookkeeping skills.";

    }

    else if(role === "graphic"){

        textarea.value =
        "Looking for Graphic Designer with Photoshop and Illustrator skills.";

    }

    else if(role === "content"){

        textarea.value =
        "Looking for Content Writer with SEO and writing skills.";

    }

    else{

        textarea.value = "";

    }

}


// Loading Screen

const form =
document.querySelector("form");

form.addEventListener("submit", function(){

    document.getElementById(
    "loadingScreen"
    ).style.display = "flex";

});