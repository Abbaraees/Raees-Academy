document.addEventListener('click', (e)=> {
    if (e.target.id == 'update-course-btn') {
        showUpdateForm()
    }
    else if (e.target.id == 'close-btn') {
        hideUpdateForm()
    }
    else if (e.target.id == 'delete-course-btn') {
        showDeleteForm()
    }
    else if (e.target.id == 'cancel-delete-btn') {
        cancelDelete()
    }
    else if (e.target.id == 'publish-btn') {
        showPublishForm()
    }
    else if (e.target.id == 'cancel-publish-btn') {
        cancelPublish()
    }

})

function showUpdateForm() {
    document.getElementById('update-course-form').style.display = 'block'
}

function hideUpdateForm() {
    document.getElementById('update-course-form').style.display = 'none'
}

function showDeleteForm() {
    document.getElementById('delete-course-form').style.display = 'block'
}

function cancelDelete() {
    document.getElementById('delete-course-form').style.display = 'none'
}

function showPublishForm() {
    document.getElementById('publish-form').style.display = 'block'
}

function cancelPublish() {
    document.getElementById('publish-form').style.display = 'none'
}
