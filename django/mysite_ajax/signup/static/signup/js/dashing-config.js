/* global $, Dashboard */

var dashboard = new Dashboard();


dashboard.addWidget('candidate_inflow_widget', 'Number', {
    getData: function () {
        $.extend(this.scope, {
            title: '3 Crore profiles from 300 locations to explore',
            //moreInfo: 'by me',
            //updatedAt: 'Last updated at 14:10',
            detail: 'Connect Now >>',
            //value: '100'
        });
    }
});
/*dashboard.addWidget('Position_Closed_widget', 'Number', {
    getData: function () {
        $.extend(this.scope, {
            title: 'Positions Closed',
            moreInfo: 'by bot',
            updatedAt: 'Last updated at 14:10',
            detail: '25% above average',
            value: '5'
        });
    }
});

dashboard.addWidget('company_widget', 'List', {
    getData: function () {
        $.extend(this.scope, {
            title: 'Trending Jobs',
            moreInfo: 'Available jobs',
            updatedAt: 'Last updated at 18:58',
            data: [{label: '1. SDE II at Amazon Prime, Bangalore', value: 58},
                   {label: '2. TPM III at Flipkart, Bangalore', value: 45},
                   {label: '3. MTS II at Oracle, Gurgaon', value: 29},
                   {label: '4. Director of Engineering at Paytm, Delhi', value: 46},
                   {label: '5. Chief Architect at Snap Deal, Bangalore', value: 23},
                   {label: '6. Technical Lead at IBM software Labs, Bangalore', value: 10},
                   {label: '7. Director of Engineering at VMWare, Bangalore', value: 4},
                   {label: '8. Support Engineer II at Oracle, Bangalore', value: 6},
                   {label: 'Also explore 1.5 lakh more openings', value: 2}]
        });
    }
});

dashboard.addWidget('candidate_widget', 'List', {
    getData: function () {
        $.extend(this.scope, {
            title: 'Trending Candidates',
            moreInfo: 'Premium Candidates',
            updatedAt: 'Last updated at 18:58',
            data: [{label: '1. Avinash Yadav, SDE II at Microsoft, Bangalore', value: 58},
                   {label: '2. Sourav Yadav, SDM III at Flipkart, Bangalore', value: 45},
                   {label: 'Also Explore 3 Crore more candidates', value: 29}]
      });
    }
});


dashboard.addWidget('completion_widget', 'Knob', {
    getData: function () {
        $.extend(this.scope, {
            title: 'Quarterly Performan',
            updatedAt: 'Last updated at 14:10',
            detail: 'today 10',
            value: '35',
            data: {
                angleArc: 250,
                angleOffset: -125,
                displayInput: true,
                displayPrevious: true,
                step: 1,
                min: 1,
                max: 99,
                readOnly: true,
                format: function(value) { return value + '%'; }
            }
        });
      }
    });

    dashboard.addWidget('Bot_Screening_Widget', 'Graph', {
    getData: function () {
        $.extend(this.scope, {
            title: 'Bot Screening Velocity',
            value: '41',
            moreInfo: '',
            data: [
                    { x: 0, y: 40 },
                    { x: 1, y: 49 },
                    { x: 2, y: 38 },
                    { x: 3, y: 30 },
                    { x: 4, y: 32 }
                ]
            });
    }
});*/
