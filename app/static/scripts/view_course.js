document.addEventListener('click', (e)=> {
    if (e.target.id == 'update-course-btn') {
        showUpdateForm()
    }
    else if (e.target.id == 'close-btn') {
        hideUpdateForm()
    }
})

function showUpdateForm() {
    document.getElementById('update-course-form').style.display = 'block'
}

function hideUpdateForm() {
    document.getElementById('update-course-form').style.display = 'none'
}