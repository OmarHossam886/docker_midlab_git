# Build stage
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /docker_midlab/worker

# copy csproj and restore
COPY Worker.csproj .
RUN dotnet restore

# copy everything else and publish
COPY . .
RUN dotnet publish Worker.csproj -c Release -o /app

# Runtime stage
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /app
COPY --from=build /app .

ENTRYPOINT ["dotnet", "Worker.dll"]
