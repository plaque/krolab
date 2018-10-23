var	express	=	require('express');
var	router	=	express.Router();


var mongoose = require('mongoose');
var Post = mongoose.model('Post');

router.route('/posts')
    .get(
        function(req,res){
            posts = [Post.findById(id, function(err, post){ return post})]
            return res.json({'posts': posts});
        }
	 );
    .post(
        function(req,res){
            return res.json({'posts': []});
        }
	 );
    .put(
        function(req,res){
            return res.json({'posts': []});
        }
	 );
    .delete(
        function(req,res){
            return res.json({'posts': []});
        }
	 );
module.exports = router;
