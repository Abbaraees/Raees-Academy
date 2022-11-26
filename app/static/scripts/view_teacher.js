/* Admin Delete Teacher */
document.addEventListener('click', function(e) {
    if (e.target.id == 'delete-teacher-btn') {
        showDeleteModal()
    } 
    else if (e.target.id == 'accept-delete') {
        deleteTeacher(e.target.dataset["teacherId"])
    }
    else if (e.target.id == 'reject-delete') {
        hideDeleteModal()
    }
    else if (e.target.id == 'edit-username') {
        document.getElementById('username-input').removeAttribute("disabled")
    }
    else if (e.target.id == 'edit-email') {
        document.getElementById('email-input').removeAttribute("disabled")
    } else if (e.target.id == 'update-button') {
        console.log(e.target.dataset)
        updateTeacher(e.target.dataset["teacherId"])
    }
    
})

document.addEventListener('change', function(e) {
    document.getElementById("update-button").removeAttribute("disabled")
})


function showDeleteModal(){
    document.getElementById('confirm-delete').style.display = 'block'
}

function hideDeleteModal() {
    document.getElementById('confirm-delete').style.display = 'none'
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