// Display msg by url parameter

let searchParams = new URLSearchParams(window.location.search)

if (searchParams.has('msg') && searchParams.has('status')) {
    let msg = searchParams.get('msg')
    let status = searchParams.get('status')

    $.toast({
        text: msg, // Text that is to be shown in the toast
        heading: 'Note', // Optional heading to be shown on the toast
        icon: status, // Type of toast icon
        showHideTransition: 'fade', // fade, slide or plain
        allowToastClose: true, // Boolean value true or false
        hideAfter: 3000, // false to make it sticky or number representing the miliseconds as time after which toast needs to be hidden
        stack: 5, // false if there should be only one toast at a time or a number representing the maximum number of toasts to be shown at a time
        position: 'top-right', // bottom-left or bottom-right or bottom-center or top-left or top-right or top-center or mid-center or an object representing the left, right, top, bottom values
        
        textAlign: 'left',  // Text alignment i.e. left, right or center
        loader: true,  // Whether to show loader or not. True by default
        loaderBg: '#9EC600',  // Background color of the toast loader
    });
}