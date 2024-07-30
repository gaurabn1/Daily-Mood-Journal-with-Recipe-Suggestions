$(document).ready(function () {
    $('#logout').on('click', function (e) {
        e.preventDefault();
        if (confirm("Are you sure?")) {
            $("#logout_form").submit();
        }
    })


    $("#edit-profile-button").on('click', function (e) {
        e.preventDefault()
        let editProfileSection = $('#edit-profile')

        if (editProfileSection.hasClass('d-none')) {
            editProfileSection.removeClass('d-none').show()
        } else {
            editProfileSection.addClass('d-none').hide()
        }
    })

    $('.delete_journal').on('click', function (e) {
        e.preventDefault()
        if (confirm("Are you sure to delete this entry?")) {
            $(this).closest('form').submit();
        }
    })

    $('#edit_journal').on('click', function (e) {
        e.preventDefault()
        $('#edit_journal_entry_textarea').toggleClass('d-none')
        $('#journal_content_entry').toggleClass('d-none')
    })

    $('#edit_journal_entry_textarea').on('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault()
            $('#edit_journal_form').submit()
        }
    })

    $('.delete-recent-entry').on('click', function(e){
        e.preventDefault()
        if(confirm("Are you sure to delete this entry?")){
            $(this).closest('form').submit()
        }
    })


})

