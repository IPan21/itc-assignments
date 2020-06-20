// import React from "react";
// import AllProductItem from "./AllProductItem"
// import { products } from './products02.json'
// import { withRouter} from "react-router";

// class AllProducts extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       allProducts: products,
//       search: null,
//       inputVal: '',
//     }
//   }

//   addToQuery(input) {
//     if (input.length == 0) {
//       this.props.history.push('/products/')
//     } else {
//       this.props.history.push('?query=' + input)
//     }
//   }

//   searchSpace=(event)=>{
//     console.log(this.state.inputVal)
//     let keyword = event.target.value;
//     this.setState({search:keyword})
//     this.setState({inputVal:keyword})
//     this.addToQuery(keyword)
//   }

//   componentDidMount() {
//     let query = this.props.location.search
//     if (query.length > 0) {
//       query = query.split('=')[1]
//       this.setState({search:query})
//       this.setState({inputVal:query})
//     }
//   }

//   render() {
//     const elementStyle ={
//       border:'solid',
//       borderRadius:'10px',
//       position:'relative',
//       height:'3vh',
//       width:'20vh',
//       marginTop:'5vh',
//       marginBottom:'10vh'
//     }

//     const { allProducts, inputVal } = this.state
//     let listToRender = allProducts.filter((data)=>{
//       if(this.state.search == null)
//           return data
//       else if(data.name.toLowerCase().includes(this.state.search.toLowerCase()) || data.description.toLowerCase().includes(this.state.search.toLowerCase())){
//           return data
//       }
//     }).map(el => <AllProductItem 
//       key={el.id} 
//       companyName={el.name} 
//       companyDescription={el.description}
//       companyDetails={el.details} />)
//     return (
//       <>
//             <div>
//       <input type="text" value={inputVal} placeholder="Enter item to be searched" style={elementStyle} onChange={(e)=>this.searchSpace(e)} />
//       {listToRender}
//       </div>
            
//       </>
//     )
//   }
// }

// export default withRouter(AllProducts);