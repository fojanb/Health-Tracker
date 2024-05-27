let flask_data,repositories;
const getRepositories = () => {
    flask_data = document.getElementById("flask_data").dataset.repositories;
    repositories = JSON.parse(flask_data);
}
const renderRepositories = () => {
    repositories.forEach((repository,index) => {
        let newRepository = document.createElement("div");
        newRepository.innerHTML = `${index + 1} - ${repository.full_name}`;
        document.body.append(newRepository);
    });
}
getRepositories();
renderRepositories();
