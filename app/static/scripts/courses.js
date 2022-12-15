document.addEventListener('click', (e)=> {
    if (e.target.id == 'show-form-btn') {
        document.getElementById("add-course-form").style.display = 'block'
    }
    else if (e.target.id == 'add-course-btn') {
        addCourse()
    }
    else if (e.target.id == 'close-btn') {
        document.getElementById("add-course-form").style.display = 'none'
    }
})

function addCourse() {
    const formData = new FormData(document.getElementById("add-course-form"))
    fetch('/teachers/add_course', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "csrf_token": formData.get('csrf_token'),
            "name": formData.get("name"),
            "description": formData.get("description")
        })
    }).then((resp) => {
        resp.json().then((data) => {
            document.getElementById("courses").innerHTML += 
                `<li><a href="/teachers/courses/${data.course['id']}">${data.course['name']}</a></li>`
            document.getElementById("add-course-form").style.display = 'none'
            document.getElementById("name").value = ""
            document.getElementById("description").value = ""
        }).catch((err)=> {
            console.log(err)
        })
    })
}