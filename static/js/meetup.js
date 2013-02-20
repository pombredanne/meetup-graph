var Meetup = new Class({
    Implements: [Options, Events],
    
    options: {},
    
    initialize: function(form, stage, options){
        this.setOptions(options);
        this.form = $(form);
        this.stage = $(stage);
        this.request = new Request.JSON();
        this.build();
    },
    
    build: function(){
        this.form.addEvent('submit', function(e){
            e.stop();
            
            this.request.options.url = this.form.get('action');
            this.request.options.method = this.form.get('method');
            this.request.removeEvents()
                .addEvent('complete', function(data){
                    this.stage.set('html', data['results']);
                }.bind(this))
                .send(this.form);
        }.bind(this));
    }
});