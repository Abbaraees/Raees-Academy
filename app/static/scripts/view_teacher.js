/* Admin Delete Teacher */
document.addEventListener('click', function(e) {
    if (e.target.id == 'delete-teacher-btn') {
        showDeleteModal()
    } 
    else if (e.target.id == 'accept-delete') {
        deleteTeacher(e)
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

function deleteTeacher(e) {
    console.log(e.target.dataset)
}