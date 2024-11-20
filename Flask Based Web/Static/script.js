$(document).ready(function() {
    $('#predict-button').click(function(event) {
        event.preventDefault();
        $('#loading-message').show(); // Show loading message

        var formData = new FormData($('#upload-form')[0]);

        $.ajax({
            type: 'POST',
            url: '/upload',
            data: formData,
            contentType: false,
            cache: false,
            processData: false,
            success: function(response) {
                $('#loading-message').hide(); // Hide loading message

                // Update the prediction results
                $('#vgg16-prediction').text('Prediction from VGG16: ' + response.vgg16_prediction);
                $('#resnet-prediction').text('Prediction from ResNet50: ' + response.resnet_prediction);
            },
            error: function(error) {
                console.log(error);
                $('#loading-message').hide(); // Hide loading message
            }
        });
    });
});
