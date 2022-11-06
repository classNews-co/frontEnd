export default async function hander(request, response) {
	response.status(200).json({
		path: request.url
	});
}
