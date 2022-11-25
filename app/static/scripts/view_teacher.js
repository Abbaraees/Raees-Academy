/* Admin Delete Teacher */
document.addEventListener('click', function(e) {
    if (e.target.id == 'delete-teacher-btn') {
        showDeleteModal()
    } 
    else if (e.target.id == 'accept-delete') {
        deleteTeacher(e.target.dataset["teacherId"])
    }
    else if ('reject-delete') {
        hideDeleteModal()
    }
    

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