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
        var self = this;
        
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
        
        this.stage.addEvent('click:relay(.node)', function(e){
            e.stop();
            
            self.request.options.url = this.get('href');
            self.request.options.mehtod = 'get';
            self.request.removeEvents()
                .addEvent('complete', function(resp){
                    self.stage.set('html', resp['results'])
                })
                .send();
        });
    },
    
    replaceStage: function(content){
        this.stage.set('html', content);
    }
});