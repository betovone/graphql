
# Documentación de uso de Django + graphQL

En el archivo **schema.graphql** están definidos los queries (consultas) y los mutations (inserts, updates y deletes).

#### URLS para ingresar:
1. http://localhost:8000/admin/: Para ingresar al admin de Django 
2. http://localhost:8000/graphql/: Para ingresar al cliente GraphQL para realizar las queries y/o mutations. En esta página tenemos ayuda de la interfaz provista por GraphQL. A la derecha existen dos botones, **DOCS** y **SCHEMA**, en los cuales se puede ir consultando que información debemos proveer para realizar bien las queries y las mutaciones.


## Queries

Consultando la documentación del botón **DOCS** se pueden realizar como ejemplo las siguientes queries:

Consultar un Post específico:
```json

query obtenerPost {
  getPost(id: "1"){
    success,
    errors,
    post{
      title,
      description
    }
  }
}
```

Listar todos los Post:
```json

{
  listPosts{
    success,
    errors,
    posts{
      id,
      title,
      description,
      created_at,
      tipo_post_id{
        description
      }
    }
  }
}
```

## Mutations

Las mutaciones son los **INSERTS**, **UPDATES** y **DELETES**.

Ejemplo de INSERT:
```json

mutation CreateNewPost {
  createPost(
    title: "New Blog Post"
    description: "Some Description"
    tipo_post_id: 1
  ) {
    post {
      id
      title
      description
      tipo_post_id {
        description
      }
    }
    success
    errors
  }
}
```

Ejemplo de UPDATE:
```json

mutation actualizarPost {
  updatePost(
    id:5,
    title: "Diario Mdz",
    description: "Diario Mdz online de mendoza"
  ){
    success,
    errors,
    post{
      id,
      title,
      description,
      created_at,
      tipo_post_id{
        description
      }
    }
  }
}
```

Ejemplo de DELETE:
```json

mutation borrarPost {
  deletePost(
    id: 3
  ){
    success,
    errors,
    post{
      id, 
      title,
      description,
      created_at,
      tipo_post_id{
        description
      }
    }
  }
}
```

Para mas información:
> https://www.apollographql.com/blog/graphql/python/complete-api-guide/







