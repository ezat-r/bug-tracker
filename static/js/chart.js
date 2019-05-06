$(function(){
    let myChart = document.getElementById("myChart").getContext("2d");

    // Global options
    Chart.defaults.global.defaultFontSize = 18;
    Chart.defaults.global.defaultFontColor = "#777";

    // Grab data from dom
    var tests = $(".chart-proj-item");

    // variables to hold label and data
    var dataSetProjLabels = []
    var dataSetData = []

    // loop through dom data and append them to relevant lists
    for(var i= 0; i<tests.length; i++){
        dataSetProjLabels.push($(tests[i]).data("project"));
        
        var count = parseInt($(tests[i]).data("count"));
        dataSetData.push(count);
    }

    // creating a pie chart, using Chart.js
    let pieChart = new Chart(myChart, {
        type: "pie",
        data: {
            labels: dataSetProjLabels,
            datasets: [{
                label: "Bug Count",
                data: dataSetData,
                backgroundColor:[
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(255, 99, 132, 0.6)'
                ]
            }],
        },
        options: {
            title:{
                display: true,
                text: "Issues / Project",
                fontSize: 22
            }
        }
    });
});