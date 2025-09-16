provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "django" {
  metadata {
    name = "face-attendance-app"
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "face-attendance-app"
      }
    }
    template {
      metadata {
        labels = {
          app = "face-attendance-app"
        }
      }
      spec {
        container {
          image = "face-attendance:latest"
          name  = "django"
          image_pull_policy = "Never"
          port {
            container_port = 8000
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "django" {
  metadata {
    name = "face-attendance-service"
  }
  spec {
    selector = {
      app = "face-attendance-app"
    }
    port {
      port      = 8000
      node_port = 30008
    }
    type = "NodePort"
  }
}