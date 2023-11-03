terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

# Define the provider
provider "google" {
  credentials = file("YOUR-SERVICE-KEY")
  project     = "YOUR-PROJECT-ID"
  region      = "YOUR-REGION"
}


# Define the artifact Registry
resource "google_artifact_registry_repository" "my-container" {
  location      = "ROUR-REGION"
  repository_id = "temp-forecast-container"
  format        = "DOCKER"
}
