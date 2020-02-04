include "sciter:reactor.tis";

class Component : Reactor.Component{
	function render() {
    return
	     <div>
	      <h1>Hello, world!</h1>
	      <h2>It is {this.data.time.toLocaleString(#time)} now.</h2>
	     </div>;
  	} 
} 