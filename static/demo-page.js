axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

var initialData = {
    agriculture: null,
    fields: null,
    workTemplates: null,
    works: [],
    choisedWork: null
};

axios.get(window.location.href + '?action=initialData')
    .then(function (response) {
        initialData.agriculture = JSON.parse(response.data.agriculture);
        initialData.fields = JSON.parse(response.data.fields);
        initialData.workTemplates = JSON.parse(response.data.works);
    });

var demoApp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#demo-app',
    data: initialData,
    methods: {
        addWork: function () {
            var currentWork = this.workTemplates[_.findIndex(this.workTemplates, ['pk', this.choisedWork])];
            this.works.push(currentWork);
            axios.get(window.location.href + '')
                .then(function (response) {

                })
        },
        popWork: function (index) {
            console.log(index);
            this.works.splice(index, 1);
        }
    }
});