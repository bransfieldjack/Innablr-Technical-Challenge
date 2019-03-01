provider "aws" {
	access_key = "${var.access_key}"
	secret_key = "${var.secret_key}"
	region = "${var.region}"
}

resource "aws_instance" "dev" {
	ami = "ami-07a3bd4944eb120a0"
	instance_type = "t2.micro"

	provisioner "remote-exec" {
		inline = [
			"sudo apt-get update",
		]
	}

}

resource "aws_instance" "testing" {
	ami = "ami-07a3bd4944eb120a0"
	instance_type = "t2.micro"
}

resource "aws_instance" "staging" {
	ami = "ami-07a3bd4944eb120a0"
	instance_type = "t2.micro"
}

resource "aws_instance" "production" {
	ami = "ami-07a3bd4944eb120a0"
	instance_type = "t2.micro"
}
