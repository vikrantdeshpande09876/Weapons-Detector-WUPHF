$(document).ready(function() {
    checkbox_name = 'MyPythonCheckbox';

    function generateServerURL(suffix) {
        /*
          DOCSTRING:  Utility function to retrieve result-URL of Flask server-page
        */
        return window.location.origin + '/' + suffix;
    }

    $("#generateConfigFile").on('click',
        function() {
            /*
              DOCSTRING:  Send the selected data over to Flask-python at backend using AJAX request
                          and finally redirect to the '/results' page
            */
            primary_parent_tag = $('input:text[name="primary_parent_tag"]')[0].value;
            primary_child_tag = $('input:text[name="primary_child_tag"]')[0].value;
            primary_key_tag = $('input:text[name="primary_key_tag"]')[0].value;
            ptags_chk = primary_parent_tag && primary_child_tag && primary_key_tag;
            nchecked_tags = $('input:checkbox[name=' + checkbox_name + ']:checked').length
            if (ptags_chk == "" || ptags_chk == null || ptags_chk == undefined || nchecked_tags == 0) {
                if (nchecked_tags == 0) {
                    alert("Please select atleast one tag from your input file!")
                } else if (primary_parent_tag == "" || primary_parent_tag == null) {
                    alert("Please fill in the static Primary Parent Tag correctly!")
                } else if (primary_child_tag == "" || primary_child_tag == null) {
                    alert("Please fill in the static Primary Child Tag correctly!")
                } else {
                    alert("Please fill in the static Primary Key Tag correctly!")
                }
                return;
            } else {
                checkboxes = $('input:checkbox[name=' + checkbox_name + ']');
                root_tag = checkboxes[0].id;
                res_array = [
                    ['Primary_Parent_Tag', primary_parent_tag, , ],
                    ['Primary_Child_Tag', primary_child_tag, , ],
                    ['Primary_Key', primary_key_tag, '' + root_tag, primary_key_tag],
                    ['Parent_Tag', '' + root_tag, '' + root_tag, '' + primary_key_tag]
                ];
                for (i = 1; i < checkboxes.length; i++) {
                    if (checkboxes[i].checked) {
                        res_array.push(['Child_Tag', '' + checkboxes[i].id, '' + root_tag, '' + primary_key_tag]);
                    }
                }
                json_res_array = { 'res_array': res_array };
                console.log("Final Array is= " + json_res_array)
                $.ajax({
                    type: 'POST',
                    url: generateServerURL('home/result'),
                    data: JSON.stringify(json_res_array),
                    datatype: 'json',
                    success: function() {
                        window.location.href = generateServerURL('result')
                    },
                }).done(function() {
                    console.log('Your data is now sent. Data=' + JSON.stringify(json_res_array));
                });
            }
        });






    $(document).delegate('#root', 'click', function() {
        /*
         DOCSTRING:  Generic handler function for clickable hierarchy of nested checkboxes
        */
        $('input[type="checkbox"]').change(function(e) {
            var checked = $(this).prop("checked"),
                container = $(this).parent(),
                siblings = container.siblings();
            container.find('input[type="checkbox"]').prop({
                indeterminate: false,
                checked: checked
            });

            function checkSiblings(el) {
                var parent = el.parent().parent(),
                    all = true;
                el.siblings().each(function() {
                    let returnValue = (all =
                        $(this)
                        .children('input[type="checkbox"]')
                        .prop("checked") === checked);
                    return returnValue;
                });
                if (all && checked) {
                    parent.children('input[type="checkbox"]').prop({
                        indeterminate: false,
                        checked: checked
                    });
                    checkSiblings(parent);
                } else if (all && !checked) {
                    parent.children('input[type="checkbox"]').prop("checked", checked);
                    parent
                        .children('input[type="checkbox"]')
                        .prop(
                            "indeterminate",
                            parent.find('input[type="checkbox"]:checked').length > 0
                        );
                    checkSiblings(parent);
                } else {
                    el.parents("li")
                        .children('input[type="checkbox"]')
                        .prop({
                            indeterminate: true,
                            checked: false
                        });
                }
            }
            checkSiblings(container);
        });
    });

});


/*
    add class for the checkboxes with classname="PrimaryKey" 
        if the xml document contains PrimaryKey in its data-value
    when user clicks submit, parse the checked checkboxes, to identify the checkbox with classname="PrimaryKey", ex: chkbx
    find its immediate parent and child with chkbx.parent() and chkbx.find("input[checkbox]").prop("checked")==checked
*/