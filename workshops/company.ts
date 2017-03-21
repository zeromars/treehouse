class Company implements IEmailable{
	name: string;
	email: string;
	constructor(companyName: string, emailAddress: string){
		this.name = companyName;
		this.email = emailAddress;
	}
}