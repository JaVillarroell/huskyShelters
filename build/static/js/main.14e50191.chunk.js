(this.webpackJsonpapp=this.webpackJsonpapp||[]).push([[0],{19:function(e,t,n){},25:function(e,t,n){"use strict";n.r(t);var s=n(2),c=n.n(s),r=n(10),a=n.n(r),i=(n(19),n(4)),o=n.n(i),j=n(9),d=n(11),h=n(12),l=n(14),u=n(13),b=n(28),x=n(27),p=n(1),O=function(e){Object(l.a)(n,e);var t=Object(u.a)(n);function n(){var e;Object(d.a)(this,n);for(var s=arguments.length,c=new Array(s),r=0;r<s;r++)c[r]=arguments[r];return(e=t.call.apply(t,[this].concat(c))).state={pets:[],isLoading:!1,images:[]},e}return Object(h.a)(n,[{key:"componentDidMount",value:function(){var e=Object(j.a)(o.a.mark((function e(){var t,n;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("https://b2rqixyao3.execute-api.us-east-1.amazonaws.com/prod/petsTable");case 2:return t=e.sent,e.next=5,t.json();case 5:n=e.sent,console.log(n),this.setState({pets:n,isLoading:!1});case 8:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"getImages",value:function(){var e=Object(j.a)(o.a.mark((function e(t){var n,s;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return this.setState({images:[],isLoading:!1}),e.next=3,fetch("https://b2rqixyao3.execute-api.us-east-1.amazonaws.com/prod/pet/"+t);case 3:return n=e.sent,e.next=6,n.json();case 6:s=e.sent,console.log(s),this.setState({images:s,isLoading:!1});case 9:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=this.state.isLoading,n=this.state.pets,s=this.state.images;if(t)return Object(p.jsx)("div",{children:"Loading..."});var c=n.map((function(t){return Object(p.jsxs)("tr",{children:[Object(p.jsx)("td",{children:t.Age}),Object(p.jsx)("td",{children:t.HealthStatus}),Object(p.jsx)("td",{children:t.Location}),Object(p.jsx)("td",{children:Object(p.jsx)(b.a,{className:"btn btn-lg btn-succes",onClick:function(){return e.getImages(t.PK)},children:"Images"})})]},t.PK)})),r=s.map((function(e){return Object(p.jsx)("tr",{children:Object(p.jsx)("td",{children:Object(p.jsx)("img",{src:"/"+e.PK+"/"+e.SK,alt:"/"+e.PK+"/"+e.SK})})},e.PK)}));return Object(p.jsxs)("div",{className:"container border-secondary rounded center",children:[Object(p.jsx)("div",{className:"row",children:Object(p.jsxs)("div",{className:"col-12 text-center",children:[Object(p.jsx)("br",{}),Object(p.jsx)("h1",{children:"HUSKY SHELTERS"}),Object(p.jsx)("h3",{}),Object(p.jsx)("br",{})]})}),Object(p.jsx)("div",{className:"row",children:Object(p.jsxs)("div",{className:".col-xs-12 center text-center",children:[Object(p.jsxs)(x.a,{responsive:!0,striped:!0,bordered:!0,children:[Object(p.jsx)("thead",{children:Object(p.jsxs)("tr",{children:[Object(p.jsx)("th",{children:"Age"}),Object(p.jsx)("th",{children:"Health Status"}),Object(p.jsx)("th",{children:"Location"})]})}),Object(p.jsx)("tbody",{children:0===this.state.pets.length?Object(p.jsx)("td",{colSpan:"9",children:"All caught up"}):c})]}),Object(p.jsx)(x.a,{responsive:!0,striped:!0,bordered:!0,children:Object(p.jsx)("tbody",{children:0===this.state.images.length?Object(p.jsx)("td",{colSpan:"9"}):r})})]})})]})}}]),n}(s.Component),g=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,29)).then((function(t){var n=t.getCLS,s=t.getFID,c=t.getFCP,r=t.getLCP,a=t.getTTFB;n(e),s(e),c(e),r(e),a(e)}))};n(24);a.a.render(Object(p.jsx)(c.a.StrictMode,{children:Object(p.jsx)(O,{})}),document.getElementById("root")),g()}},[[25,1,2]]]);
//# sourceMappingURL=main.14e50191.chunk.js.map