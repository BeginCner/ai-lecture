package com.sk.catndog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import ch.qos.logback.core.model.Model;

@Controller
public class MainController {
	@GetMapping("/select")
	public String upload(Model model) throws Exception {
		return "classifier";
	}

}
