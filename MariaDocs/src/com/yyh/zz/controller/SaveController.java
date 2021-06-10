package com.yyh.zz.controller;

import com.yyh.zz.dao.contentDAO;
import com.yyh.zz.model.Content;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.Map;


/**
 * @author 叶菸淮
 */
@Controller
public class SaveController {
	private Content content;
	
	@Resource 
	private contentDAO contentdao;

    /**
     * 通过spring mvc request mapping, 跳转到前台index.jsp
     * @throws Exception
     */
	@RequestMapping("/index")
	public String toLoginPage()throws Exception {
 		return "index";
	}

    /**
     * 初始化最新数据
     */
    @ResponseBody
    @RequestMapping(value = "initdata", method = RequestMethod.POST)
 	public Content toInitData(){
		this.content = new Content();
		this.content.setScontent(contentdao.search());
		System.out.println("content:"+contentdao.search());
		return content;
	}

    /**
     * 手动保存
     */
    @RequestMapping(value="save", method = {RequestMethod.POST} ,produces = "text/html;charset=UTF-8") 
    @ResponseBody  
	 public  Map<String, Object> doSave(@RequestBody String initcontent) {   
    	boolean state = contentdao.insert(initcontent); 
    	Map<String, Object> modelMap = new HashMap<String, Object>();  
        modelMap.put("state", state);  
        return modelMap;  
	 } 

}
