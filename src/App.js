import React, { Component } from 'react';
import {Table, Button} from 'reactstrap'

class App extends Component {

	/*
	state = { 
		isLoading: false,
		pets: [
			{
				"petId": "pet_001",
				"type": "Dog",
				"age": "3",
				"healthStatus": "Healthy",
				"location": "London",
				"pictures": '["https://picsum.photos/200?image=2","https://picsum.photos/200?image=2","https://picsum.photos/200?image=2"]'
			},
			{
				"petId": "pet_002",
				"type": "Dog",
				"age": "3",
				"healthStatus": "Healthy",
				"location": "London",
				"pictures": '["https://picsum.photos/200?image=2","https://picsum.photos/200?image=2","https://picsum.photos/200?image=2"]'
			},
			{
				"petId": "pet_003",
				"type": "Dog",
				"age": "3",
				"healthStatus": "Healthy",
				"location": "London",
				"pictures": '["https://picsum.photos/200?image=2","https://picsum.photos/200?image=2","https://picsum.photos/200?image=2"]'
			},
			{
				"petId": "pet_004",
				"type": "Dog",
				"age": "3",
				"healthStatus": "Healthy",
				"location": "London",
				"pictures": '["https://picsum.photos/200?image=2","https://picsum.photos/200?image=2","https://picsum.photos/200?image=2"]'
			}
		]
	}
*/

	state = {
		pets: [],
		isLoading: false,
		images: []
	}


	async componentDidMount(){
		const response = await fetch('https://b2rqixyao3.execute-api.us-east-1.amazonaws.com/prod/petsTable');
		const body = await response.json();
		console.log(body)
		this.setState({pets:body, isLoading:false})
	}

	async getImages(petPK){
		this.setState({images:[], isLoading:false})
		const response = await fetch('https://b2rqixyao3.execute-api.us-east-1.amazonaws.com/prod/pet/'+petPK);
		const body = await response.json();
		console.log(body)
		this.setState({images:body, isLoading:false})
	}

	render() {

		const isLoading = this.state.isLoading;
		const allPets = this.state.pets
		const allImages = this.state.images

		if (isLoading)
			return(<div>Loading...</div>);


		
		let pets = 
		allPets.map( pet => 
			<tr key={pet.PK}>
				<td>{pet.PK}</td>
				<td>{pet.Age}</td>
				<td>{pet.HealthStatus}</td>
				<td>{pet.LocationPet}</td>
				<td><Button className="btn btn-lg btn-succes" onClick={() => this.getImages(pet.PK)}>Images</Button></td>
			</tr>
		)

		let imgs = 
		allImages.map( pet => 
			<tr key={pet.PK}>
				<td><img src={"https://huskysheltersawsbucket50.s3.amazonaws.com/images/"+pet.PK+"/"+pet.SK} alt={"/"+pet.PK+"/"+pet.SK}></img></td>
			</tr>
		)


		return (
			<div className="container border-secondary rounded center">

				<div className="row">
					<div className="col-12 text-center">
						<br></br>
						<h1>HUSKY SHELTERS</h1>
						<h3></h3>
						<br></br>
					</div>
				</div>

				<div className="row">
					<div className=".col-xs-12 center text-center">
						<Table responsive striped bordered>
							<thead>
								<tr>
									<th>Age</th>
									<th>Health Status</th>
									<th>Location</th>
								</tr>
							</thead>

							<tbody>
								{this.state.pets.length === 0 ? <td colSpan="9">All caught up</td> : pets}
							</tbody>
						</Table>
						<Table responsive striped bordered>
							<tbody>
								{this.state.images.length === 0 ? <td colSpan="9"></td> : imgs}
							</tbody>
						</Table>
					</div>
				</div>

			</div>
		);
	}
}

export default App;
