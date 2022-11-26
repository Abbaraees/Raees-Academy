/* Admin Delete Teacher */
document.addEventListener('click', function(e) {
    if (e.target.id == 'delete-teacher-btn') {
        showModal('confirm-delete')
    } 
    else if (e.target.id == 'accept-delete') {
        deleteTeacher(e.target.dataset["teacherId"])
    }
    else if (e.target.id == 'reject-delete') {
        hideModal('confirm-delete')
    }
    else if (e.target.id == 'edit-username') {
        document.getElementById('username-input').removeAttribute("disabled")
    }
    else if (e.target.id == 'edit-email') {
        document.getElementById('email-input').removeAttribute("disabled")
    } else if (e.target.id == 'update-button') {
        updateTeacher(e.target.dataset["teacherId"])
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