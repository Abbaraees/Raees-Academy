document.addEventListener('click', function(e) {
    if (e.target.id == 'delete-teacher-btn') {
        showModal('confirm-delete')
    } 
    else if (e.target.id == 'accept-delete') {
        if (e.target.dataset["target"] == "student") {
            deleteStudent()
        }
        else deleteTeacher(e.target.dataset["teacherId"])
    }
    else if (e.target.id == 'reject-delete') {
        hideModal('confirm-delete')
    }
    else if (e.target.className == 'edit-button') {
        editInput(e.target.dataset['inputId'])
    }
    else if (e.target.id == 'update-button') {
        if (e.target.dataset['target'] == 'student') {
            updateStudent()
        }
        else updateTeacher(e.target.dataset["teacherId"])
    }
    else if (e.target.id == 'reset-password-btn') {
        showModal('confirm-reset')
    }
    else if (e.target.id == 'reject-reset') {
        hideModal('confirm-reset')
    } 
    else if (e.target.id == 'accept-reset') {
        resetTeacherPassword()
    }
    
})

function editInput(inputId) {
    document.getElementById(inputId).removeAttribute("disabled")
}

document.addEventListener('change', function(e) {
    document.getElementById("update-button").removeAttribute("disabled")
})


function showModal(modalId){
    if (modalId == 'confirm-delete') {
        document.getElementById('confirm-delete').style.display = 'block'
    }
    else if (modalId == 'confirm-reset') {
        document.getElementById('confirm-reset').style.display = 'block'
    }
}

function hideModal(modalId) {
    if (modalId == 'confirm-delete') {
        document.getElementById('confirm-delete').style.display = 'none'
    }
    else if (modalId == 'confirm-reset') {
        document.getElementById('confirm-reset').style.display = 'none'
    }
}

function deleteTeacher(teacherId) {
    fetch('/admin/teachers/delete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"id": teacherId})
    }).then((resp) => {
        window.location = resp.url
    })
}

function updateTeacher(teacherId) {
    const username = document.getElementById("username-input").value
    const email = document.getElementById("email-input").value
    fetch('/admin/teachers/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "id": teacherId,
            "username": username,
            "email": email
        })
    }).then((resp) => {
        window.location = resp.url
    })
}

function resetTeacherPassword() {
    document.getElementById('reset-password-form').submit()
}

function updateStudent() {
    editInput("firstname-input")
    editInput("lastname-input")
    editInput("email-input")
    editInput("username-input")
    const updateForm = document.getElementById("update-form").submit()
}

function deleteStudent() {
    document.getElementById("delete-user-form").submit()
}